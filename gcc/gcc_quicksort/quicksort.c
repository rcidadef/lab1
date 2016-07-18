#include <stdlib.h>
#include <stdio.h>
#define N 99999999




void qSortInterno(int v[], int inicio, int fim);

/* Funcao qickSort a ser chamada em outros pontos do programa. Serve apenas para disparar a chamada revursiva */


void quickSort(int v[], int n) {

  qSortInterno(v, 0, n-1);

}

/* Implementacao do quicksort em si. */

void qSortInterno(int v[], int inicio, int fim) {
  int pivot;
  int temp;
  int i,j;

  if(fim - inicio > 0) {
    i = inicio;
    j = fim;
    pivot = v[(i+j)/2];

    do {
      while(v[i] < pivot) i++; /* procura por algum item do lado errado  >= pivot */
      while(v[j] > pivot) j--; /* procura por algum item do lado errado <= pivot */
      if(i<= j) { /* deixa o igual para garantir que ao final i<j */
	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
	i++; j--;
      }
    } while (i<=j);

    if(inicio < j) qSortInterno(v,inicio, j);
    if(i < fim) qSortInterno(v, i,fim);
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
  quickSort(v, N);
  printf("ordenacao concluida.\n");
  
}


