#include<iostream>
#include<vector>

using namespace std;

void swap(int* a, int* b){
	int *c = a;
	*a = *b;
	*b = *c;
}

void Quicksort(vector<int>& elements, int left, int right){
	if(left < right){
		int pivot = elements[right];
		int i = left - 1;
		
		for(int j = left ; j < right; j++){
			if(elements[j] < pivot){
				i++;
				swap(elements.at(j), elements.at(i));
			}
		}

		swap(elements.at(i+1), elements.at(right));
		Quicksort(elements, left, i);
		Quicksort(elements, i+2, right);
	}
}

void printElements(vector<int> elements){
	cout << endl;
	for(auto n: elements){
		cout << n << "\t";
	}	
	cout << endl;
}

int main(){
	vector<int> numbers = {10,15,1,2,6,12,5,7};

	//Printing the original values
	printElements(numbers);

	Quicksort(numbers, 0, numbers.size() - 1);

	//Values after quicksort
	printElements(numbers);

	return 0;
}
