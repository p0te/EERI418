
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim){
	double dt = 100000*(0.000001);
	double sum =0;
		int k = 0;
	HAL_ADC_Start(&hadc1);
	HAL_ADC_Start(&hadc2);
	int duty = 50;
double div = 256/2.8667;
	double V1 = 0;
	double V2 = 0;
	char temp1[50];
	char temp2[50];
	V1 = (double)HAL_ADC_GetValue(&hadc1); //ADC on PA2
	V2 = (double)HAL_ADC_GetValue(&hadc2); //ADC on PA3
	
	while(k <10000)
	{
	sum += (double)HAL_ADC_GetValue(&hadc2); //ADC on PA3
	k++;
	}
	V2 = sum/10000;
	V1 = (V1/div);
	V2 = (V2/div);
	double ERROR = V1-V2;
	integral = integral + (ERROR*dt);
	double kp = 160;
	double ki = 90;
	double out = kp*ERROR + ki*integral;
	if(out-prePWM > 2){out = prePWM + 2;}
	if(out-prePWM < 2){out = prePWM - 2;}
	sprintf(temp1,"OUT = %f \t PREOUT = %f \t ERROR = %f \t TACHO = %f \t SOURCE = %f \n",(out),(prePWM),(ERROR),(V2), V1);
		if (out > 100){out = 100;}
	if (out < 0){	out = 0;}
	TIM1->CCR1 = round(100-out);
	prePWM = out;
//sprintf(temp1,"V1 = %f \n V2 = %f \n ERROR = %f \n INTEGRAL = %f \n OUT = %f \n",(V1),(V2),(ERROR),(integral),(out));
trace(temp1,50);
//MX_TIM1_Init();
	//MX_ADC1_Init();
	//trace("Interrupt!\n",11);
}
/* USER CODE END 4 */

