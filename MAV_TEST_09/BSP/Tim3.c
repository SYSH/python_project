#include "tim3.h"

u32 TIM4_IRQCNT = 0;
/**************************ʵ�ֺ���********************************************
*����ԭ��:		
*��������:1ms�ж�һ��,������Ϊ1000		
*******************************************************************************/
void Tim4_Init(u16 period_num)
{
	TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;
	//�������ã�ʱ���ͱȽ�������ã���������ֻ�趨ʱ�����Բ���OC�Ƚ����
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4,ENABLE);
	
	TIM_DeInit(TIM4);

	TIM_TimeBaseStructure.TIM_Period=period_num;//װ��ֵ
	//prescaler is 1200,that is 72000000/72/500=2000Hz;
	TIM_TimeBaseStructure.TIM_Prescaler=72-1;//��Ƶϵ��
	//set clock division 
	TIM_TimeBaseStructure.TIM_ClockDivision=TIM_CKD_DIV1; //or TIM_CKD_DIV2 or TIM_CKD_DIV4
	//count up
	TIM_TimeBaseStructure.TIM_CounterMode=TIM_CounterMode_Up;
	
	TIM_TimeBaseInit(TIM4,&TIM_TimeBaseStructure);
	//clear the TIM4 overflow interrupt flag
	TIM_ClearFlag(TIM4,TIM_FLAG_Update);
	//TIM4 overflow interrupt enable
	TIM_ITConfig(TIM4,TIM_IT_Update,ENABLE);
	//enable TIM4
	//TIM_Cmd(TIM3,ENABLE);
}
void Tim4_Control(u8 sta)
{
	if(0==sta)
		TIM_Cmd(TIM4,DISABLE);
	if(1==sta)
		TIM_Cmd(TIM4,ENABLE);
}
