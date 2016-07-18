#include <stdio.h>
#include <stdlib.h>
#define N 99999999

int PesquisaBinaria ( int k[], int chave , int t)
{
 int inf,sup,meio;
 inf=0;
 sup=N-1;
 while (inf<=sup)
 {
      meio=(inf+sup)/2;
      if (chave==k[meio])
           return meio;
      else if (chave<k[meio])
           sup=meio-1;
      else
           inf=meio+1;
 }
 return -1;   /* não encontrado */
}

int main() {
  int *v;
  int i;
  int resp = 0;
  srand(0);

  v = (int*) malloc (sizeof(int)*N);
  for(i = 0; i< N; i++) {
    v[i]= rand();
  }
 
  

  printf("Buscar...\n");
  resp = PesquisaBinaria(v,44,N);
  if (resp == -1){
  printf("nao encontrou!.\n");
  }
}

