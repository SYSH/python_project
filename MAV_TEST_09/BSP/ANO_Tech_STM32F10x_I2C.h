#ifndef __STM32_I2C_H
#define __STM32_I2C_H
#include "stm32f10x.h"
/*====================================================================================================*/
/*====================================================================================================*/
uint8_t ANO_Tech_I2C1_Write_Int(uint8_t DevAddr, uint8_t RegAddr, uint8_t WriteNum, uint8_t * WriteTemp);
//I2Cд���ֽڣ����IIC��æ����0���������д�ɹ�������1
uint8_t ANO_Tech_I2C1_Write_1Byte(uint8_t DevAddr, uint8_t RegAddr, uint8_t WriteData);
uint8_t ANO_Tech_I2C1_Write_Buf(uint8_t DevAddr, uint8_t RegAddr, uint8_t WriteNum, uint8_t * WriteTemp);
//I2Cд���ֽڣ��ȴ�д������ɺ󷵻أ���ɺ󣬷���1
uint8_t ANO_Tech_I2C1_Read_Int(uint8_t DevAddr, uint8_t RegAddr, uint8_t ReadNum, uint8_t * ReadTemp);
//I2C�����ֽڻ���ֽڣ���������1������ʱ��ȡ�����ܿ��ܻ�δ��ɣ�
uint8_t ANO_Tech_I2C1_Read_Buf(uint8_t DevAddr, uint8_t RegAddr, uint8_t ReadNum, uint8_t * ReadTemp);
//I2C�����ֽڻ���ֽڣ���ȡ��ɺ󷵻�1
void ANO_Tech_I2C1_EV_IRQ( void );
//I2C1�¼��ж�,��I2C1_EV_IRQHandler�ж��е��ñ�����
void ANO_Tech_I2C1_ER_IRQ( void );
//I2C1�����ж�,��I2C1_ER_IRQHandler�ж��е��ñ�����
/*====================================================================================================*/
/*====================================================================================================*/
#endif
