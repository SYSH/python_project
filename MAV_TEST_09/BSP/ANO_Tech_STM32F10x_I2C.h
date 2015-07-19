#ifndef __STM32_I2C_H
#define __STM32_I2C_H
#include "stm32f10x.h"
/*====================================================================================================*/
/*====================================================================================================*/
uint8_t ANO_Tech_I2C1_Write_Int(uint8_t DevAddr, uint8_t RegAddr, uint8_t WriteNum, uint8_t * WriteTemp);
//I2C写多字节，如果IIC正忙返回0，如果触发写成功，返回1
uint8_t ANO_Tech_I2C1_Write_1Byte(uint8_t DevAddr, uint8_t RegAddr, uint8_t WriteData);
uint8_t ANO_Tech_I2C1_Write_Buf(uint8_t DevAddr, uint8_t RegAddr, uint8_t WriteNum, uint8_t * WriteTemp);
//I2C写多字节，等待写操作完成后返回，完成后，返回1
uint8_t ANO_Tech_I2C1_Read_Int(uint8_t DevAddr, uint8_t RegAddr, uint8_t ReadNum, uint8_t * ReadTemp);
//I2C读单字节或多字节，立即返回1（返回时读取操作很可能还未完成）
uint8_t ANO_Tech_I2C1_Read_Buf(uint8_t DevAddr, uint8_t RegAddr, uint8_t ReadNum, uint8_t * ReadTemp);
//I2C读单字节或多字节，读取完成后返回1
void ANO_Tech_I2C1_EV_IRQ( void );
//I2C1事件中断,在I2C1_EV_IRQHandler中断中调用本函数
void ANO_Tech_I2C1_ER_IRQ( void );
//I2C1错误中断,在I2C1_ER_IRQHandler中断中调用本函数
/*====================================================================================================*/
/*====================================================================================================*/
#endif
