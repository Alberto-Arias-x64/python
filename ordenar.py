#include <stdio.h> 
#include <math.h> 
  
#/* Función de insertion Sort*/
def insertionSort(arr,n):
   for i in range(n):
       currentVal= arr[i] #//obtenemos el valor actual a comparar
       j = i-1
       #/* mueve los elementos del arreglo arr[0..i-1],que son mayores que el valor de la posición actual del recorrido, a una posición adelante de su posición actual */
       while (j >= 0 and arr[j] > currentVal):
           arr[j+1] = arr[j]
           j = j-1
       arr[j+1] = currentVal
  
def printArray(arr,n):

   for i in range(n):
       print(arr[i])
   print()
  
  

if __name__ == "__main__":

    arr = [6, 4, 3, 11, 10]
    n = len(arr)
  
    insertionSort(arr, n)
    printArray(arr, n)
