#include <stdio.h>

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

union{

	float f;
	
	struct
	{
		unsigned int mant: 23;
		unsigned int exp : 8;
		unsigned int sign: 1;

	}
} helper2;

void floatOut(){
	printf("++++++++++++++++++++++++++++++++++++++++++++++++++++	\n");
	printf("value: "); printf("%f",helper.f);printf("\n");
	printf("mantissa_lo: "); printf("%i",helper.mantissa_lo);printf("\n");
	printf("mantissa_hi: "); printf("%i",helper.mantissa_hi);printf("\n");
	printf("exponent: "); printf("%i",helper.mantissa_hi);printf("\n");
	printf("sign: "); printf("%i",helper.mantissa_hi);printf("\n");
	printf("++++++++++++++++++++++++++++++++++++++++++++++++++++    \n");
}

int main(){

		helper.f = 20;
		floatOut();
		
		helper.f = 0;
		floatOut();

		helper.f = 100;
		floatOut();
		
		helper.f = -10;
		floatOut();

		helper.f = 2.898;
		floatOut();


		printf("++++++++++++++++++++++++++++++++++++++++");

		helper.f = 20;
		unsigned long mantissa = helper.mantissa_lo;
		printf("\n");
		printf("%i" , mantissa);
		printf("\n");
		printf("%i" ,helper.mantissa_hi);
		printf("\n");
		printf("((unsigned long) helper.mantissa_hi << 16) = ");printf("%i" , ((unsigned long) helper.mantissa_hi << 16));
		printf("\n");
		mantissa += ((unsigned long) helper.mantissa_hi << 16);
		mantissa += 0x00800000;
		signed char exponent = (signed char) helper.exponent - 127;

		printf("\n");
		printf("%i", mantissa);
		printf("\n");
		printf("%i" , exponent);
		printf("\n");

		printf("+++++++++++++++++++++++++++++++++++++++");
		helper2.f = 20;
		printf("\n");
		printf("%i" , helper2.mant);
		printf("\n");
	return 0;
}
