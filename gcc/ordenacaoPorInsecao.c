#include <stdlib.h>
#include <stdio.h>
#define N 99999


void ordenaInsercao(int  v[], int tamanho) {
    int i, j;
    int pivot;


    for(j = 1; j < tamanho; j++ ) {
      i = j -1;
      pivot = v[j];
      while(i>=0) {
	if(v[i]>pivot) {
	  v[i+1] = v[i];
	}
	else {
	  break;
	}
	i--;
      }
      v[i+1] = pivot;
    }
  }

 int main() {
  int *v;
  int i;
  srand(0);

  v = (int*) malloc (sizeof(int)*N);
  for(i = 0; i< N; i++) {
    v[i]= rand();
  }

  printf("iniciando ordenacao...\n");
  ordenaInsercao(v, N);
  printf("ordenacao concluida.\n");
  
}
