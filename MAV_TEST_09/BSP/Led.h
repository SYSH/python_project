#ifndef _LED_H_
#define _LED_H_
#include "stm32f10x.h"
#include "tim3.h"		

#define LED1_OFF  	GPIO_SetBits(GPIOB, GPIO_Pin_12)
#define LED1_ON 		GPIO_ResetBits(GPIOB, GPIO_Pin_12)

#define LEDALL_OFF  GPIO_SetBits(GPIOB, GPIO_Pin_12 )
#define LEDALL_ON 	GPIO_ResetBits(GPIOB, GPIO_Pin_12 )

void LED_INIT(void);
void LED_FLASH(void);
void LED1_ONOFF(void);

#endif
