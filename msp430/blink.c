#include <msp430x20x2.h>

void main(void){
   WDTCTL = WDTPW + WDTHOLD;	// Stop watchdog timer
   P1DIR |= 0x41;

   for (;;){
      volatile unsigned int i;
      
      P1OUT ^= 0x41;		// Toggle P1.0 using exclusive-OR

      i = 50000;		// Delay
      do (i--);
      while (i != 0);
   }
}
