#include "MPU6050.h"
#include "ANO_Tech_STM32F10x_I2C.h"

static u8				mpu6050_buffer[14];					//iic��ȡ��������
T_int16_xyz		GYRO_OFFSET,ACC_OFFSET;			//��Ư
static u8				GYRO_OFFSET_OK = 1;
static u8				ACC_OFFSET_OK = 1;

void Delay_ms_mpu(u16 nms)
{	
	uint16_t i,j;
	for(i=0;i<nms;i++)
		for(j=0;j<8500;j++);
} 
void MPU6050_CalOff_Acc(void)
{
	ACC_OFFSET_OK = 0;
}
void MPU6050_CalOff_Gyr(void)
{
	GYRO_OFFSET_OK = 0;
}
/**************************ʵ�ֺ���********************************************
//��iic��ȡ�������ݷֲ�,������Ӧ�Ĵ���
*******************************************************************************/
#define 	MPU6050_MAX		32767
#define		MPU6050_MIN		-32768
void MPU6050_Dataanl(T_int16_xyz *data_tempacc,T_int16_xyz *data_tempgyr)
{
	vs32 acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z;
	
	acc_x=((((int16_t)mpu6050_buffer[0]) << 8) | mpu6050_buffer[1]) - ACC_OFFSET.X;
	acc_y=((((int16_t)mpu6050_buffer[2]) << 8) | mpu6050_buffer[3]) - ACC_OFFSET.Y;
	acc_z=((((int16_t)mpu6050_buffer[4]) << 8) | mpu6050_buffer[5]) - ACC_OFFSET.Z;
	//????ADC
	gyr_x=((((int16_t)mpu6050_buffer[8]) << 8) | mpu6050_buffer[9]) - GYRO_OFFSET.X;
	gyr_y=((((int16_t)mpu6050_buffer[10]) << 8) | mpu6050_buffer[11]) - GYRO_OFFSET.Y;
	gyr_z=((((int16_t)mpu6050_buffer[12]) << 8) | mpu6050_buffer[13]) - GYRO_OFFSET.Z;
	
	acc_x>MPU6050_MAX ? MPU6050_MAX:acc_x;
	acc_x<MPU6050_MIN ? MPU6050_MIN:acc_x;
	acc_y>MPU6050_MAX ? MPU6050_MAX:acc_y;
	acc_y<MPU6050_MIN ? MPU6050_MIN:acc_y;
	acc_z>MPU6050_MAX ? MPU6050_MAX:acc_z;
	acc_z<MPU6050_MIN ? MPU6050_MIN:acc_z;
	gyr_x>MPU6050_MAX ? MPU6050_MAX:gyr_x;
	gyr_x<MPU6050_MIN ? MPU6050_MIN:gyr_x;
	gyr_y>MPU6050_MAX ? MPU6050_MAX:gyr_y;
	gyr_y<MPU6050_MIN ? MPU6050_MIN:gyr_y;
	gyr_z>MPU6050_MAX ? MPU6050_MAX:gyr_z;
	gyr_z<MPU6050_MIN ? MPU6050_MIN:gyr_z;
	
	data_tempacc->X = acc_x;
	data_tempacc->Y = acc_y;
	data_tempacc->Z = acc_z;
	data_tempgyr->X = gyr_x;
	data_tempgyr->Y = gyr_y;
	data_tempgyr->Z = gyr_z;
	
	if(!GYRO_OFFSET_OK)    //������У׼
	{
		static int32_t	tempgx=0,tempgy=0,tempgz=0;
		static uint8_t cnt_g=0;
// 		LED1_ON;
		if(cnt_g==0)
		{
			GYRO_OFFSET.X=0;
			GYRO_OFFSET.Y=0;
			GYRO_OFFSET.Z=0;
			tempgx = 0;
			tempgy = 0;
			tempgz = 0;
			cnt_g = 1;
			return;
		}
		tempgx+= data_tempgyr->X;
		tempgy+= data_tempgyr->Y;
		tempgz+= data_tempgyr->Z;
		if(cnt_g==200)//200��ֵ��ƽ��
		{
			GYRO_OFFSET.X=tempgx/cnt_g;
			GYRO_OFFSET.Y=tempgy/cnt_g;
			GYRO_OFFSET.Z=tempgz/cnt_g;
			cnt_g = 0;
			GYRO_OFFSET_OK = 1;
			EE_SAVE_GYRO_OFFSET();//��������
			return;
		}
		cnt_g++;
	}
	if(!ACC_OFFSET_OK)    //���ٶ�У׼
	{
		static int32_t	tempax=0,tempay=0,tempaz=0;
		static uint8_t cnt_a=0;
// 		LED1_ON;
		if(cnt_a==0)
		{
			ACC_OFFSET.X = 0;
			ACC_OFFSET.Y = 0;
			ACC_OFFSET.Z = 0;
			tempax = 0;
			tempay = 0;
			tempaz = 0;
			cnt_a = 1;
			return;
		}
		tempax+= data_tempacc->X;
		tempay+= data_tempacc->Y;
		//tempaz+= MPU6050_ACC_LAST.Z;
		if(cnt_a==200)
		{
			ACC_OFFSET.X=tempax/cnt_a;
			ACC_OFFSET.Y=tempay/cnt_a;
			ACC_OFFSET.Z=tempaz/cnt_a;
			cnt_a = 0;
			ACC_OFFSET_OK = 1;
			EE_SAVE_ACC_OFFSET();//��������
			return;
		}
		cnt_a++;		
	}
}
/**************************ʵ�ֺ���********************************************
//��iic��ȡ�������ݷֲ�,������Ӧ�Ĵ���,����MPU6050_Last
*******************************************************************************/
void MPU6050_Read(void)
{
	ANO_Tech_I2C1_Read_Int(devAddr,ACCEL_XOUT_H,14,mpu6050_buffer);// Ӳ��I2C��ȡ����������
	//I2C_ReadBuffer(mpu6050_buffer, 0x3B, 14);// I2C��ѯ��ʽ��ȡ����������
}
/*
*******************************************************************************************
                    Ӳ��I2Cʹ�õĺ���
*******************************************************************************************
*/
/**************************ʵ�ֺ���********************************************
*����ԭ��:		u8 IICwriteBit(u8 dev, u8 reg, u8 bitNum, u8 data)
*��������:	    �� �޸� д ָ���豸 ָ���Ĵ���һ���ֽ� �е�1��λ
����	dev  Ŀ���豸��ַ
reg	   �Ĵ�����ַ
bitNum  Ҫ�޸�Ŀ���ֽڵ�bitNumλ
data  Ϊ0 ʱ��Ŀ��λ������0 ���򽫱���λ
����   �ɹ� Ϊ1 
ʧ��Ϊ0
*******************************************************************************/ 
void IICwriteBit(u8 dev, u8 reg, u8 bitNum, u8 data){
	u8 b;
	ANO_Tech_I2C1_Read_Buf(dev, reg, 1, &b);
	b = (data != 0) ? (b | (1 << bitNum)) : (b & ~(1 << bitNum));
	ANO_Tech_I2C1_Write_Buf(dev, reg,1,&b);
}
/**************************ʵ�ֺ���********************************************
*����ԭ��:		u8 IICwriteBits(u8 dev,u8 reg,u8 bitStart,u8 length,u8 data)
*��������:	    �� �޸� д ָ���豸 ָ���Ĵ���һ���ֽ� �еĶ��λ
����	dev  Ŀ���豸��ַ
reg	   �Ĵ�����ַ
bitStart  Ŀ���ֽڵ���ʼλ
length   λ����
data    ��Ÿı�Ŀ���ֽ�λ��ֵ
����   �ɹ� Ϊ1 
ʧ��Ϊ0
*******************************************************************************/ 
void IICwriteBits(u8 dev,u8 reg,u8 bitStart,u8 length,u8 data)
{
	
	u8 b,mask;
	ANO_Tech_I2C1_Read_Buf(dev, reg, 1, &b);
	mask = (0xFF << (bitStart + 1)) | 0xFF >> ((8 - bitStart) + length - 1);
	data <<= (8 - length);
	data >>= (7 - bitStart);
	b &= mask;
	b |= data;
	ANO_Tech_I2C1_Write_Buf(dev, reg,1,&b);
}
/**************************ʵ�ֺ���********************************************
*����ԭ��:		void MPU6050_setClockSource(uint8_t source)
*��������:	    ����  MPU6050 ��ʱ��Դ
* CLK_SEL | Clock Source
* --------+--------------------------------------
* 0       | Internal oscillator
* 1       | PLL with X Gyro reference
* 2       | PLL with Y Gyro reference
* 3       | PLL with Z Gyro reference
* 4       | PLL with external 32.768kHz reference
* 5       | PLL with external 19.2MHz reference
* 6       | Reserved
* 7       | Stops the clock and keeps the timing generator in reset
*******************************************************************************/
void MPU6050_setClockSource(uint8_t source){
	IICwriteBits(devAddr, PWR_MGMT_1, MPU6050_PWR1_CLKSEL_BIT, MPU6050_PWR1_CLKSEL_LENGTH, source);
	
}
/** Set full-scale gyroscope range.
* @param range New full-scale gyroscope range value
* @see getFullScaleRange()
* @see MPU6050_GYRO_FS_250
* @see GYRO_CONFIG
* @see MPU6050_GCONFIG_FS_SEL_BIT
* @see MPU6050_GCONFIG_FS_SEL_LENGTH
*/
void MPU6050_setFullScaleGyroRange(uint8_t range) {
	IICwriteBits(devAddr, GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH, range);
}

/**************************ʵ�ֺ���********************************************
*����ԭ��:		void MPU6050_setFullScaleAccelRange(uint8_t range)
*��������:	    ����  MPU6050 ���ٶȼƵ��������
*******************************************************************************/
void MPU6050_setFullScaleAccelRange(uint8_t range) {
	IICwriteBits(devAddr, ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH, range);
}
/**************************ʵ�ֺ���********************************************
*����ԭ��:		void MPU6050_setSleepEnabled(uint8_t enabled)
*��������:	    ����  MPU6050 �Ƿ����˯��ģʽ
enabled =1   ˯��
enabled =0   ����
*******************************************************************************/
void MPU6050_setSleepEnabled(uint8_t enabled) {
	IICwriteBit(devAddr, PWR_MGMT_1, MPU6050_PWR1_SLEEP_BIT, enabled);
}

/**************************ʵ�ֺ���********************************************
*����ԭ��:		void MPU6050_setI2CMasterModeEnabled(uint8_t enabled)
*��������:	    ���� MPU6050 �Ƿ�ΪAUX I2C�ߵ�����
*******************************************************************************/
void MPU6050_setI2CMasterModeEnabled(uint8_t enabled) {
	IICwriteBit(devAddr, USER_CTRL, MPU6050_USERCTRL_I2C_MST_EN_BIT, enabled);
}

/**************************ʵ�ֺ���********************************************
*����ԭ��:		void MPU6050_setI2CBypassEnabled(uint8_t enabled)
*��������:	    ���� MPU6050 �Ƿ�ΪAUX I2C�ߵ�����
*******************************************************************************/
void MPU6050_setI2CBypassEnabled(uint8_t enabled) {
	IICwriteBit(devAddr, INT_PIN_CFG, MPU6050_INTCFG_I2C_BYPASS_EN_BIT, enabled);
}

void MPU6050_setDLPF(uint8_t mode)
{
	IICwriteBits(devAddr, MPUCONFIG, MPU6050_CFG_DLPF_CFG_BIT, MPU6050_CFG_DLPF_CFG_LENGTH, mode);
}
/**************************ʵ�ֺ���********************************************
*����ԭ��:		void MPU6050_initialize(void)
*��������:	    ��ʼ�� 	MPU6050 �Խ������״̬��
*******************************************************************************/
void MPU6050_Init(void)
{

	MPU6050_setSleepEnabled(0); //���빤��״̬
	Delay_ms_mpu(200);
	MPU6050_setClockSource(MPU6050_CLOCK_PLL_XGYRO); //����ʱ��  0x6b   0x01
	Delay_ms_mpu(50);
	MPU6050_setFullScaleGyroRange(MPU6050_GYRO_FS_2000);//������������� +-2000��ÿ��
	Delay_ms_mpu(50);
	MPU6050_setFullScaleAccelRange(MPU6050_ACCEL_FS_4);	//���ٶȶ�������� +-4G
	Delay_ms_mpu(50);
	MPU6050_setDLPF(MPU6050_DLPF_BW_42);
	Delay_ms_mpu(50);
	MPU6050_setI2CMasterModeEnabled(0);	 //����MPU6050 ����AUXI2C
	Delay_ms_mpu(50);
	MPU6050_setI2CBypassEnabled(1);	 //����������I2C��	MPU6050��AUXI2C	ֱͨ������������ֱ�ӷ���HMC5883L
	Delay_ms_mpu(50);
}

/*
*******************************************************************************************
                    I2C��ѯ��ʽʹ�õĺ���
*******************************************************************************************
*/
//void MPU6050_Init(void)//MPU6050��ʼ��
//{
//	I2C_WriteByte(PWR_MGMT_1, 0x01);  //��Դ�������������������  ʱ��ΪPLL with X axis gyroscope reference
//	Delay_ms_mpu(10);
//	I2C_WriteByte(SMPLRT_DIV, 0x00);  //1KHz ����Ƶ��Sample Rate = Gyroscope Output Rate / (1 + SMPLRT_DIV)  Gyroscope Output Rate=1KHz
//	I2C_WriteByte(MPUCONFIG, 0x03);   //DLPF����  ACC����44HZ,��ʱ��4.9ms  GYR����42Hz����ʱ��4.8ms  ������ʣ�1KHz
// 	I2C_WriteByte(GYRO_CONFIG, 0x18); //�������Լ켰������Χ�����Լ죬+-2000deg/s
// 	I2C_WriteByte(ACCEL_CONFIG, 0x08);//���ټ��Լ졢������Χ,���Լ죬+-4g
//	I2C_WriteByte(USER_CTRL, 0x40);   //ʹ��FIFO ������MPU6050����AUXI2C
//	I2C_WriteByte(INT_PIN_CFG, 0x02); //����I2C��MPU6050AUXI2Cֱͨ������������ֱ�ӷ���HMC5883L
//}

void I2C_WriteByte(uint8_t REG_Address,uint8_t Write_Data )
{
  /* Send STRAT condition */
  I2C_GenerateSTART(I2C1, ENABLE);

  /* Test on EV5 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_MODE_SELECT));  

  /* Send EEPROM address for write */
  I2C_Send7bitAddress(I2C1, I2C1_MPU6050, I2C_Direction_Transmitter);
  
  /* Test on EV6 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_TRANSMITTER_MODE_SELECTED));
  
  /* Send the EEPROM's internal address to write to : only one byte Address */
  I2C_SendData(I2C1, REG_Address);
  
  /* Test on EV8 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_BYTE_TRANSMITTED));

  /* Send the byte to be written */
  I2C_SendData(I2C1, Write_Data); 
   
  /* Test on EV8 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_BYTE_TRANSMITTED));
  
  /* Send STOP condition */
  I2C_GenerateSTOP(I2C1, ENABLE);  
}

uint8_t I2C_ReadByte(uint8_t REG_Address)
{
	uint8_t data_byte;
  //*((u8 *)0x4001080c) |=0x80; 
  while(I2C_GetFlagStatus(I2C1, I2C_FLAG_BUSY)); // Added by Najoua 27/08/2008
    
    
  /* Send START condition */
  I2C_GenerateSTART(I2C1, ENABLE);
  //*((u8 *)0x4001080c) &=~0x80;
  
  /* Test on EV5 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_MODE_SELECT));

  /* Send EEPROM address for write */
  I2C_Send7bitAddress(I2C1, I2C1_MPU6050, I2C_Direction_Transmitter);

  /* Test on EV6 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_TRANSMITTER_MODE_SELECTED));
  
  /* Clear EV6 by setting again the PE bit */
  I2C_Cmd(I2C1, ENABLE);

  /* Send the EEPROM's internal address to write to */
  I2C_SendData(I2C1, REG_Address);  

  /* Test on EV8 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_BYTE_TRANSMITTED));
  
  /* Send STRAT condition a second time */  
  I2C_GenerateSTART(I2C1, ENABLE);
  
  /* Test on EV5 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_MODE_SELECT));
  
  /* Send EEPROM address for read */
  I2C_Send7bitAddress(I2C1, I2C1_MPU6050, I2C_Direction_Receiver);
  
  /* Test on EV6 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_RECEIVER_MODE_SELECTED));
  
  /* While there is data to be read */
       /* Disable Acknowledgement */
      I2C_AcknowledgeConfig(I2C1, DISABLE);
      
      /* Send STOP Condition */
      I2C_GenerateSTOP(I2C1, ENABLE);

    /* Test on EV7 and clear it */
    if(I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_BYTE_RECEIVED))       
      /* Read a byte from the EEPROM */
      data_byte = I2C_ReceiveData(I2C1);


  /* Enable Acknowledgement to be ready for another reception */
  I2C_AcknowledgeConfig(I2C1, ENABLE);
	//I2C_EE_WaitEepromStandbyState();
	return data_byte;
}

void I2C_ReadBuffer(uint8_t* Data_Buffer, uint8_t REG_Address, uint8_t Num_Byte)
{  
  //*((u8 *)0x4001080c) |=0x80; 
  while(I2C_GetFlagStatus(I2C1, I2C_FLAG_BUSY)); // Added by Najoua 27/08/2008
    
    
  /* Send START condition */
  I2C_GenerateSTART(I2C1, ENABLE);
  //*((u8 *)0x4001080c) &=~0x80;
  
  /* Test on EV5 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_MODE_SELECT));

  /* Send EEPROM address for write */
  I2C_Send7bitAddress(I2C1, I2C1_MPU6050, I2C_Direction_Transmitter);

  /* Test on EV6 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_TRANSMITTER_MODE_SELECTED));
  
  /* Clear EV6 by setting again the PE bit */
  I2C_Cmd(I2C1, ENABLE);

  /* Send the EEPROM's internal address to write to */
  I2C_SendData(I2C1, REG_Address);  

  /* Test on EV8 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_BYTE_TRANSMITTED));
  
  /* Send STRAT condition a second time */  
  I2C_GenerateSTART(I2C1, ENABLE);
  
  /* Test on EV5 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_MODE_SELECT));
  
  /* Send EEPROM address for read */
  I2C_Send7bitAddress(I2C1, I2C1_MPU6050, I2C_Direction_Receiver);
  
  /* Test on EV6 and clear it */
  while(!I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_RECEIVER_MODE_SELECTED));
  
  /* While there is data to be read */
  while(Num_Byte)  
  {
    if(Num_Byte == 1)
    {
      /* Disable Acknowledgement */
      I2C_AcknowledgeConfig(I2C1, DISABLE);
      
      /* Send STOP Condition */
      I2C_GenerateSTOP(I2C1, ENABLE);
    }

    /* Test on EV7 and clear it */
    if(I2C_CheckEvent(I2C1, I2C_EVENT_MASTER_BYTE_RECEIVED))  
    {      
      /* Read a byte from the EEPROM */
      *Data_Buffer = I2C_ReceiveData(I2C1);

      /* Point to the next location where the byte read will be saved */
      Data_Buffer++; 
      
      /* Decrement the read bytes counter */
      Num_Byte--;        
    }   
  }

  /* Enable Acknowledgement to be ready for another reception */
  I2C_AcknowledgeConfig(I2C1, ENABLE);
	//I2C_EE_WaitEepromStandbyState();
}

/*
*******************************************************************************************
*******************************************************************************************
*/
void I2C1_Congiguration(void)
{
  GPIO_InitTypeDef  GPIO_InitStructure; 
	I2C_InitTypeDef  I2C_InitStructure; 
  /* I2C Periph clock enable */
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_I2C1, ENABLE);   
  
  /* GPIO Periph clock enable */
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB , ENABLE);    
	
  /* Configure I2C1 pins: SCL and SDA */
  GPIO_InitStructure.GPIO_Pin =  GPIO_Pin_6 | GPIO_Pin_7; 
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_OD;
  GPIO_Init(GPIOB, &GPIO_InitStructure);
	
	/* I2C configuration */
  I2C_InitStructure.I2C_Mode = I2C_Mode_I2C;
  I2C_InitStructure.I2C_DutyCycle = I2C_DutyCycle_2;
  I2C_InitStructure.I2C_OwnAddress1 = I2C_SLAVE_ADDRESS7;
  I2C_InitStructure.I2C_Ack = I2C_Ack_Enable;
  I2C_InitStructure.I2C_AcknowledgedAddress = I2C_AcknowledgedAddress_7bit;
  I2C_InitStructure.I2C_ClockSpeed = I2C_Speed;
  
  /* I2C Peripheral Enable */
  I2C_Cmd(I2C1, ENABLE);
  /* Apply I2C configuration after enabling it */
  I2C_Init(I2C1, &I2C_InitStructure);
	/*����1�ֽ�Ӧ��ģʽ*/
	I2C_AcknowledgeConfig(I2C1, ENABLE);  	
	/* Enable I2C1 event and error interrupts */
  I2C_ITConfig(I2C1, I2C_IT_EVT | I2C_IT_ERR, ENABLE);
}
