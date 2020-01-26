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

//for( helper.f = -1000.0f ; helper.f < 1000.0f; helper.f++ )
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

	return 0;
}
