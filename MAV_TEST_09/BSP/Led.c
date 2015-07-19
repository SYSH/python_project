#include "led.h"

void Delay_ms_led(u16 nms)
{	
	uint16_t i,j;
	for(i=0;i<nms;i++)
		for(j=0;j<8500;j++);
} 

void LED_INIT(void)
{
	 GPIO_InitTypeDef  GPIO_InitStructure;	
	 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);	 //使能PB端口时钟
		
	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_12;				       //LED0-->PB.12 端口配置
	 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		   //推挽输出
	 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	 GPIO_Init(GPIOB, &GPIO_InitStructure);
}

void LED_FLASH(void)
{
	LED1_ON;
	Delay_ms_led(100);
	LED1_OFF;
	Delay_ms_led(100);
	LED1_ON;
	Delay_ms_led(100);
	LED1_OFF;
	Delay_ms_led(100);
	LED1_ON;
	Delay_ms_led(100);
	LED1_OFF;
	Delay_ms_led(100);
	LED1_ON;
	Delay_ms_led(100);
	LED1_OFF;
	Delay_ms_led(100);
	LED1_ON;
	Delay_ms_led(100);
	LED1_OFF;
	Delay_ms_led(100);
	LED1_ON;
	Delay_ms_led(100);
	LED1_OFF;
	Delay_ms_led(100);
}
void LED1_ONOFF(void)
{
	static uint8_t busy=0;
	static uint8_t led1_sta=1;
	static uint32_t time_temp;
	if(led1_sta)
	{
		if(!busy)
		{
			time_temp=TIM4_IRQCNT;
			busy=1;
		}
		else if((time_temp+150)<TIM4_IRQCNT)//200 on time
		{
			led1_sta=0;
			LED1_OFF;
			busy=0;
		}
	}
	else
	{
		if(!busy)
		{
			time_temp=TIM4_IRQCNT;
			busy=1;
		}
		else if((time_temp+150)<TIM4_IRQCNT)
		{
			led1_sta=1;
			LED1_ON;
			busy=0;
		}
	}
}
