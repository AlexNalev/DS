#include<iostream>

using std::cout;
using std::cin;
using std::endl;

class Node{
	public:
		int data;
		Node* next;
		
		Node(int data, Node* next = NULL){
			this->data = data;
			this->next = next;
		}
};

class Queue{
	Node* front_queue;
	Node* back_queue;

	public:
		Queue(){
			front_queue = NULL;
			back_queue = NULL;
		}

		void enqueue(int data){
			if(front_queue == NULL){
				front_queue = new Node(data);
				back_queue = front_queue;
			}

			else{
				Node* traversal = front_queue;
				while(traversal->next != NULL){
					traversal = traversal->next;
				}
					
				//Now we are at the back_queue of the queue
				traversal->next = new Node(data);
				back_queue = traversal->next;
			}
		}

		void dequeue(){
			if(front_queue == NULL){
				cout << "Underflow state\n";
			}

			else{
				Node* traversal = front_queue;
				front_queue = front_queue->next;
				delete traversal;				
			}
		}
		
		int front(){
			return front_queue->data;
		}
		
		int back(){
			return back_queue->data;
		}

		void show_elements(){
			if(front_queue == NULL){
				cout << "Empty queue\n";
			}

			else{
				Node* traversal = front_queue;

				while(traversal != NULL){
					cout << traversal-> data << endl;
					traversal = traversal->next;
				}
			}
		}

		~Queue(){
			if(front_queue != NULL){
				while(front_queue != NULL){
					Node* traversal = front_queue;
					front_queue = front_queue->next;
					delete traversal;
				}
				back_queue = front_queue;
			}
		}
};

int main(){
Queue line;
line.show_elements();
line.enqueue(1);
line.enqueue(2);
line.enqueue(3);
line.enqueue(4);
line.dequeue();
line.show_elements();
line.dequeue();
line.dequeue();
line.dequeue();
line.show_elements();
return 0;
}

