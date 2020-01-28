#include <stdlib.h>

union{
  
      float f;
      
      struct
      {
          unsigned int mant: 23; 
          unsigned int exp : 8;
          unsigned int sign: 1;
  
      }   
} helper2;

union{
      float f;

      struct
      {
          unsigned int    mantissa_lo: 16;
          unsigned int    mantissa_hi: 7;
          unsigned int    exponent : 8;
          unsigned int    sign: 1;
      };
} helper;


int main(){

	for(int i = 0 ; i < 100; i++){
	
		printf("+++++++++++++++++++++++++++++++++++++++++++=");

		float number = rand() % 2000;
		number /= (rand()%5);

		printf("\nrand numbner is "); printf("%f" , number);
		
		printf("\n");
		helper.f = number;
		unsigned long mantissa = helper.mantissa_lo;
		mantissa += ((unsigned long) helper.mantissa_hi << 16);
		mantissa += 0x00800000;
		printf("chelick mantissa "); printf("%i" , mantissa);

		printf("\n");

		helper2.f = number;	
		mantissa = helper2.mant;
		mantissa += 8388608;
		printf("Fedor mantissa ");	printf("%i" ,mantissa);
		printf("\n+++++++++++++++++++++++++++++++++++++++++++=");
	}
}
