#include<stdio.h>
#include<conio.h>
#define MAX 100
int BinarySearch(int arr[],int left,int right,int target) {
    while(left<=right) {
	int mid = left+(right-left)/2;
	if(arr[mid]==target) {
	    return mid;
	}
	else if(arr[mid]<target) {
	    left=mid+1;
	}
	else {
	    right = mid - 1;
	}
    }
    return -1;
}
int main() {
    int arr[MAX], n, a, i, result;
    clrscr();
    printf("Enter size of array: ");
    scanf("%d",&n);
    printf("Enter array: ");
    for(i=0;i<n;i++)
	scanf("%d",&arr[i]);
    printf("Enter element to be searched: ");
    scanf("%d",&a);
    result=BinarySearch(arr,0,n-1,a);
    if(result!=-1) {
	printf("Element is found at index %d",result);
    }
    else {
	printf("Element not found");
    }
    getch();
    return 0;
}