#include<conio.h>
#include<stdio.h>
#define MAX 100

void main()
{
    int a[MAX],n,key,i,c=0;
    clrscr();
    printf("Enter size of array: ");
    scanf("%d", &n);
    printf("Enter Array: ");
    for(i=0;i<n;i++)
	    scanf("%d",&a[i]);
    printf("Enter no. to be searched: ");
    scanf("%d", &key);
    for(i=0;i<n;i++)
    {
	if(a[i]==key)
	{
	    printf("Element found at position %d",i);
	    c++;
	}
    }
    if(c==0)
	printf("Elememt not found.");
    getch();
}