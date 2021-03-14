#include<iostream>
#include<vector>

using namespace std;

void swap(int* a, int* b){
	int *c = a;
	*a = *b;
	*b = *c;
}

void Quicksort(vector<int>& elements, int left, int right){
	if(left == right){
		return
	}
	else{
		int pivot = elements[right];
		int i = left - 1;
		
		for(int j = left ; j < right; j++){
			if(elements[j] < pivot){
				i++;
				swap(elements.at(j), elements.at(i));
			}
		}

		swap(elements.at(i+1), elements.at(right);
		Quicksort(elements, left, i);
		Quicksort(elements, i+2, right);
	}
}

void printElements(vector<int> elements){
	for(auto n: elements){
		cout << n << "\t";
	}	
}

int main(){
	vector<int> numbers = {7,2,1,8,6,3,5,4};
	//Printing the original values
	printElements(numbers);
	Quicksort(numbers, )
	printElements(numbers, 0, numbers.size() - 1);

	return 0;
}
