#include "rc.h"

void Rc_Fun(T_RC_Data *rc_in,T_RC_Control *rc_ct)
{
	static u8 cnt_arm=0,cnt_fun=0;
	if(rc_in->THROTTLE<RC_FUN_MIN&&rc_in->YAW<RC_FUN_MIN)  //���ڽ����ɿ�
	{																											 
		cnt_arm++;
		if(cnt_arm==75)
		{
			cnt_arm=0;
			rc_ct->ARMED = 1;
		}
	}
	else if(rc_in->THROTTLE<RC_FUN_MIN&&rc_in->YAW>RC_FUN_MAX)  //���ڸ��ɿ�����
	{
		cnt_arm++;
		if(cnt_arm==75)
		{
			cnt_arm=0;
			rc_ct->ARMED = 0;
		}
	}
	else
		cnt_arm = 0;
		
	if(rc_ct->ARMED==1)
		return;
	
	if(rc_in->THROTTLE<RC_FUN_MIN&&rc_in->ROLL<RC_FUN_MIN)   //RC_FUN_MIN=1200
	{
		cnt_fun++;
		if(cnt_fun==75)
		{
			cnt_fun = 0;
			MPU6050_CalOff_Acc();   //ACC У׼��ƫ��־Ϊ0
		}
	}
	else if(rc_in->THROTTLE<RC_FUN_MIN&&rc_in->ROLL>RC_FUN_MAX) //RC_FUN_MAX=1800
	{
		cnt_fun++;
		if(cnt_fun==75)
		{
			cnt_fun = 0;
			MPU6050_CalOff_Gyr();  //Gyr У׼��ƫ��־Ϊ0
		}
	}
	else
		cnt_fun = 0;
}
