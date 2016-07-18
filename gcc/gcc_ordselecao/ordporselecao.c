#include <stdlib.h>
#include <stdio.h>
#define N 99999


void selectionSort(int vetor[],int tam) {
   int i, j;
   int min, aux;
   for(i=0; i<tam-1; i++) {
      min = i;
      for(j=i+1; j<tam; j++) {
        if (vetor[j] < vetor[min])
           min=j;
      }
      aux = vetor[i];
      vetor[i] = vetor[min];
      vetor[min] = aux;
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
  selectionSort(v, N);
  printf("ordenacao concluida.\n"); 
}
