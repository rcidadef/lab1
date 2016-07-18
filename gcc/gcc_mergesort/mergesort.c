#include <stdio.h>
#include <stdlib.h>
#define N 9999999

void intercala(int v[], int vaux[], int inicio, int fim, int meio) {
  int i, j,k;

  k = inicio;
  i = inicio;
  j = meio+1;

  while((i <= meio) && (j <= fim)) {

    if(v[i] < v[j]) {
      vaux[k] = v[i];
      i++;
    }
    else {
      vaux[k]= v[j];
      j++;
    }
    k++;
  }

  while(i<=meio) {
    vaux[k] = v[i];
    i++; 
    k++;
  }

  while(j <= fim) {
    vaux[k]= v[j];
    j++;
    k++;
  }
  for(k = inicio; k <=fim; k++) {
    v[k]=vaux[k];
  }
}
 
void mergeSortInterno(int v[], int vaux[], int inicio, int fim) {
  int meio;

  if(inicio < fim) {
    meio = (inicio+fim)/2;
    mergeSortInterno(v,vaux,inicio, meio);
    mergeSortInterno(v,vaux, meio+1,fim);
    intercala(v,vaux,inicio,fim,meio);
  }
}


void mergeSort(int v[], int n) {
  int *vaux;

  vaux = (int*) malloc(sizeof(int)*n);

  mergeSortInterno(v,vaux,0,n-1);
  free(vaux);

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
  mergeSort(v, N);
  printf("ordenacao concluida.\n");
  
}

