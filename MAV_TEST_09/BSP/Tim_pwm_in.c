#include "tim_pwm_in.h"

static u16 			Rc_Pwm_In[4];
static T_RC_Data 	Rc_Data;//1000~2000

static void Rc_DataAnl(void)           //该函数可以重定义四通道与输入口的对应关系
{																			 //使接收机与TIM捕捉到硬件连接统一起来
    Rc_Data.PITCH	   =	Rc_Pwm_In[0];
		Rc_Data.ROLL	   =	Rc_Pwm_In[1];
		Rc_Data.THROTTLE =	Rc_Pwm_In[2];
		Rc_Data.YAW			 =	Rc_Pwm_In[3];	
}
void Rc_GetValue(T_RC_Data *temp)
{
	temp->THROTTLE	= Rc_Data.THROTTLE;
	temp->YAW		    = Rc_Data.YAW;
	temp->ROLL		  = Rc_Data.ROLL;
	temp->PITCH		  = Rc_Data.PITCH;	
}
void Tim_Pwm_In_Init(void)
{
	TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;
	TIM_ICInitTypeDef  TIM_ICInitStructure;
	GPIO_InitTypeDef GPIO_InitStructure;

	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3,ENABLE);

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA|RCC_APB2Periph_GPIOB, ENABLE);

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6|GPIO_Pin_7;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
	GPIO_Init(GPIOA, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_1;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
	GPIO_Init(GPIOB, &GPIO_InitStructure);

	TIM_DeInit(TIM3);

	TIM_TimeBaseStructure.TIM_Period = 0xffff;	//???
	//CLK = 72000000/TIM_Prescaler
	TIM_TimeBaseStructure.TIM_Prescaler=71;//
	//set clock division 
	TIM_TimeBaseStructure.TIM_ClockDivision=TIM_CKD_DIV1; //or TIM_CKD_DIV2 or TIM_CKD_DIV4
	//count up
	TIM_TimeBaseStructure.TIM_CounterMode=TIM_CounterMode_Up;
	
	TIM_TimeBaseInit(TIM3,&TIM_TimeBaseStructure);
	
	TIM_ICInitStructure.TIM_Channel = TIM_Channel_1;
	TIM_ICInitStructure.TIM_ICPolarity = TIM_ICPolarity_BothEdge;
	TIM_ICInitStructure.TIM_ICSelection = TIM_ICSelection_DirectTI;	
	TIM_ICInitStructure.TIM_ICPrescaler = TIM_ICPSC_DIV1;     
	TIM_ICInitStructure.TIM_ICFilter = 0x0;       
	TIM_ICInit(TIM3, &TIM_ICInitStructure);
	
	TIM_ICInitStructure.TIM_Channel = TIM_Channel_2;
	TIM_ICInitStructure.TIM_ICPolarity = TIM_ICPolarity_BothEdge;
	TIM_ICInitStructure.TIM_ICSelection = TIM_ICSelection_DirectTI;	
	TIM_ICInitStructure.TIM_ICPrescaler = TIM_ICPSC_DIV1;     
	TIM_ICInitStructure.TIM_ICFilter = 0x0;       
	TIM_ICInit(TIM3, &TIM_ICInitStructure);
	
	TIM_ICInitStructure.TIM_Channel = TIM_Channel_3;
	TIM_ICInitStructure.TIM_ICPolarity = TIM_ICPolarity_BothEdge;
	TIM_ICInitStructure.TIM_ICSelection = TIM_ICSelection_DirectTI;	
	TIM_ICInitStructure.TIM_ICPrescaler = TIM_ICPSC_DIV1;     
	TIM_ICInitStructure.TIM_ICFilter = 0x0;       
	TIM_ICInit(TIM3, &TIM_ICInitStructure);
	
	TIM_ICInitStructure.TIM_Channel = TIM_Channel_4;
	TIM_ICInitStructure.TIM_ICPolarity = TIM_ICPolarity_BothEdge;
	TIM_ICInitStructure.TIM_ICSelection = TIM_ICSelection_DirectTI;	
	TIM_ICInitStructure.TIM_ICPrescaler = TIM_ICPSC_DIV1;     
	TIM_ICInitStructure.TIM_ICFilter = 0x0;       
	TIM_ICInit(TIM3, &TIM_ICInitStructure);

	/* TIM enable counter */
	TIM_Cmd(TIM3, ENABLE);
	/* Enable the CC1 Interrupt Request */
	TIM_ITConfig(TIM3, TIM_IT_CC1, ENABLE);
	TIM_ITConfig(TIM3, TIM_IT_CC2, ENABLE);
	TIM_ITConfig(TIM3, TIM_IT_CC3, ENABLE);
	TIM_ITConfig(TIM3, TIM_IT_CC4, ENABLE);

}
void Tim3_Pwm_In_Irq(void)
{
	static u16 temp_cnt1,temp_cnt1_2,temp_cnt2,temp_cnt2_2,temp_cnt3,temp_cnt3_2,temp_cnt4,temp_cnt4_2;
	
	if(TIM3->SR & TIM_IT_CC1)
	{
		u16 ccr1 = TIM3->CCR1;
		TIM3->SR &= ~TIM_FLAG_CC1OF;
		if(GPIOA->IDR & GPIO_Pin_6)
		{
			temp_cnt1 = ccr1;
			TIM3->CCER |= (1<<1);
		}
		else
		{
			temp_cnt1_2 = ccr1;
			TIM3->CCER &= ~(1<<1);
			if(temp_cnt1_2>=temp_cnt1)
				Rc_Pwm_In[0] = temp_cnt1_2-temp_cnt1;
			else
				Rc_Pwm_In[0] = 0xffff-temp_cnt1+temp_cnt1_2;
		}
	}
	if(TIM3->SR & TIM_IT_CC2)
	{
		u16 ccr2 = TIM3->CCR2;
		if(GPIOA->IDR & GPIO_Pin_7)
		{
			temp_cnt2 = ccr2;
			TIM3->CCER |= (1<<5);
		}
		else
		{
			temp_cnt2_2 = ccr2;
			TIM3->CCER &= ~(1<<5);
			if(temp_cnt2_2>=temp_cnt2)
				Rc_Pwm_In[1] = temp_cnt2_2-temp_cnt2;
			else
				Rc_Pwm_In[1] = 0xffff-temp_cnt2+temp_cnt2_2;
		}
	}
	if(TIM3->SR & TIM_IT_CC3)
	{
		u16 ccr3 = TIM3->CCR3;
		if(GPIOB->IDR & GPIO_Pin_0)
		{
			temp_cnt3 = ccr3;
			TIM3->CCER |= (1<<9);
		}
		else
		{
			temp_cnt3_2 = ccr3;
			TIM3->CCER &= ~(1<<9);
			if(temp_cnt3_2>=temp_cnt3)
				Rc_Pwm_In[2] = temp_cnt3_2-temp_cnt3;
			else
				Rc_Pwm_In[2] = 0xffff-temp_cnt3+temp_cnt3_2;
		}
	}
	if(TIM3->SR & TIM_IT_CC4)
	{
		u16 ccr4 = TIM3->CCR4;
		if(GPIOB->IDR & GPIO_Pin_1)
		{
			temp_cnt4 = ccr4;
			TIM3->CCER |= (1<<13);
		}
		else
		{
			temp_cnt4_2 = ccr4;
			TIM3->CCER &= ~(1<<13);
			if(temp_cnt4_2>=temp_cnt4)
				Rc_Pwm_In[3] = temp_cnt4_2-temp_cnt4;
			else
				Rc_Pwm_In[3] = 0xffff-temp_cnt4+temp_cnt4_2;
				
			Rc_DataAnl();
		}		
	}	
}
