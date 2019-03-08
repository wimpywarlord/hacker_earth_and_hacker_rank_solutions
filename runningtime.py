#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int insertionsort(int *a, int n) {
  int i;
  int value;
  int hole;
  int shift = 0;
  for (i = 1; i < n; i++) {
    value = a[i];
    hole = i;
    while (hole > 0 && a[hole - 1] > value) {
      a[hole] = a[hole - 1];
      hole = hole - 1;
      shift++;
    }
    a[hole] = value;
  }
  return shift;
}
int main() {

  int n;
  int *a;
  int i;
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++)
    scanf("%d", (a + i));
  printf("%d", insertionsort(a, n));
  return 0;
}
