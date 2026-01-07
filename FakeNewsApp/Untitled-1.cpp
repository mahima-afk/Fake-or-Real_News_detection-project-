

class Student {
private:
    int roll;
    string name;
    static int count;  

public:
  
    Student(int r, string n) {
        roll = r;
        name = n;
        count++;   
    }
    void display() {
        cout << "Roll No: " << roll << ", Name: " << name << endl;
    }
    static void showCount() {
        cout << "Total number of students: " << count << endl;
    }
};
int Student::count = 0;

int main() {
    Student s1(1, "Neha");
    Student s2(2, "Ravi");
    Student s3(3, "Anita");

    s1.display();
    s2.display();
    s3.display();
    Student::showCount();

    return 0;
}