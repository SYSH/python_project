/* Includes ------------------------------------------------------------------*/
#include "stm32f10x.h"
#include "sysconfig.h"
#include "bsp.h"
#include "led.h"
#include "tim3.h"	
#include "usart.h"
#include "MPU6050.h"
#include "moto.h"
#include "spi.h"
#include "nrf24l01.h"
#include "tim_pwm_in.h"
#include "rc.h"
#include "imu.h"
#include "control.h"
#include "data_transfer.h"

u8 SYS_INIT_OK=0;
////////////////////////////////////////////////////////////////////////////////
void SYS_INIT(void)
{

	LED_INIT();
	LED_FLASH();
	Uart1_Init(115200);	
	Moto_Init();
	Tim4_Init(500);
#ifdef CONTROL_USE_RC
	Tim_Pwm_In_Init();
#endif

#ifdef DATA_TRANSFER_USE_SPI_NRF
	SPI2_Init();
	Nrf24l01_Init(MODEL_TX2,40);
 	while(!Nrf24l01_Check())									
		Uart1_Put_String("NRF24L01 IS NOT OK !\r\n");
	Uart1_Put_String("NRF24L01 IS OK !\r\n");	
#endif

	Nvic_Init();
	I2C1_Congiguration();
	MPU6050_Init();
	FLASH_Unlock();
	EE_INIT();
	EE_READ_ACC_OFFSET();
	EE_READ_GYRO_OFFSET();
	EE_READ_PID();
	Tim4_Control(1);
}
////////////////////////////////////////////////////////////////////////////////
u8 FLAG_ATT=0;
T_int16_xyz 		Acc,Gyr;	  //两次求平均后的传感器数据
T_int16_xyz			Acc_AVG;    //20次求平均后的ACC数据
T_float_angle 	Att_Angle;	//ATT函数计算出的姿态角
vs32				Alt;
T_RC_Data 			Rc_D;		//遥控通道数据
T_RC_Control		Rc_C;		//遥控功能数据
int main(void)
{
	static u8 att_cnt=0;
	static u8 rc_cnt=0;
	static T_int16_xyz mpu6050_dataacc1,mpu6050_dataacc2,mpu6050_datagyr1,mpu6050_datagyr2;
	static u8 senser_cnt=0,status_cnt=0,dt_rc_cnt=0,dt_moto_cnt=0;
		
	SYS_INIT();
	
	while (1)
	{			     
		if(FLAG_ATT)  //0.5ms 进入一次
		{
 			FLAG_ATT = 0;
			att_cnt++;
			rc_cnt++;
			if(rc_cnt==20)   //10ms 获取一次接收机数据
			{
				rc_cnt = 0;
				#ifdef CONTROL_USE_RC
				Rc_GetValue(&Rc_D);   //获取接收机数据
				#endif
				Rc_Fun(&Rc_D,&Rc_C);  //解锁/上锁/校准判定
			}
			if(att_cnt==1)
				MPU6050_Dataanl(&mpu6050_dataacc1,&mpu6050_datagyr1);   //预处理MPU6050数据
			else
			{
				att_cnt = 0;
				MPU6050_Dataanl(&mpu6050_dataacc2,&mpu6050_datagyr2);
				Acc.X = (mpu6050_dataacc1.X+mpu6050_dataacc2.X)/2;//两次采集数据求平均
				Acc.Y = (mpu6050_dataacc1.Y+mpu6050_dataacc2.Y)/2;
				Acc.Z = (mpu6050_dataacc1.Z+mpu6050_dataacc2.Z)/2;
				Gyr.X = (mpu6050_datagyr1.X+mpu6050_datagyr2.X)/2;
				Gyr.Y = (mpu6050_datagyr1.Y+mpu6050_datagyr2.Y)/2;
				Gyr.Z = (mpu6050_datagyr1.Z+mpu6050_datagyr2.Z)/2;
				Prepare_Data(&Acc,&Acc_AVG);         //获取20次ACC数据求平均  即为20ms
				IMUupdate(&Gyr,&Acc_AVG,&Att_Angle); //四元数求取Yaw、Pitch、Roll角度
				Control(&Att_Angle,&Gyr,&Rc_D,Rc_C.ARMED);
				if(Rc_C.ARMED)
					LED1_ONOFF();
				else
					LED1_OFF;					
				senser_cnt++;
				status_cnt++;
				dt_rc_cnt++;
				dt_moto_cnt++;
				if(senser_cnt==5)        //5ms 进行一次传感器数据传送 
				{
					senser_cnt = 0;
					Send_Senser = 1;
				}
				if(status_cnt==5)        //5ms 进行一次状态数据传送
				{
					status_cnt = 0;
					Send_Status = 1;
				}
				if(dt_rc_cnt==10)        //10ms 进行一次RC数据传送
				{
					dt_rc_cnt=0;
					Send_RCData = 1;
				}
				if(dt_moto_cnt==10)      //10ms 进行一次Moto数据传送
				{
					dt_moto_cnt=0;
					Send_MotoPwm = 1;
				}
			}
		}
	}
}
////////////////////////////////////////////////////////////////////////////////

