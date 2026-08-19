import java.util.Scanner;

public class StaticArray {

    static int count = 0; //Track how many slots are filled 
    public static void main(String[] args) {
        //int  index = -1;

        Scanner scanner = new Scanner(System.in);

        //WE will create an array of integers and print its size
        System.out.println("Enter the size of the array: ");
        //Ask to the user to enter the size of the array
        int size = Integer.parseInt(scanner.nextLine());

        //Now we create the array with the size entered by the user
        int[] array = new int[size];

        //Now we can fill the array in one class and search in another class
        //But we need a menu to be show always until the user wanted to exit so for the first time we can do
        String flag = "Y";
        do{
            System.out.println("\n----------------------------------------------------------");
            System.out.println("Options with the array:");
            System.out.println("----------------------------------------------------------\n");
            System.out.println("1. Fill all the array");
            System.out.println("2. Fill the array with one element");
            System.out.println("3. Search an element");
            System.out.println("4. See the elements of the array");
            System.out.println("5. Exit");
            System.out.println("----------------------------------------------------------\n");
            
            int option = Integer.parseInt(scanner.nextLine());
            int element;
            switch (option) {
                case 1:
                    fillArray(array);
                    break;
                case 2:
                    System.out.println("Type the element to put inside");
                    element = Integer.parseInt(scanner.nextLine());
                    filloneArray(array, element);
                    break;
                case 3:
                    System.out.println("Type the element to find");
                    element = Integer.parseInt(scanner.nextLine());
                    int temp = findElement(array, element);
                    if (temp!=-1){
                        System.out.println("The index of the element is: " + temp);
                    }else{
                        System.out.println("Element is not on the array");
                    }
                    break;
                case 4:
                    printArray(array);
                    break;
                case 5:
                    flag = "N";
                    break;
            }
        }while(flag.equals("Y"));
        System.out.println("Later");
    }


    //Method to fill the array with values
    public static void fillArray(int[] array) {
        Scanner scanner = new Scanner(System.in);
        //Check if array is full
        if(count >= array.length) {
            System.out.println("The array is full");
            return; //AS we have check and we are going to return we do not have to put an else instruction
        }
        System.out.println("Enter the elements of the array: ");
        //Instead of begining at 0 begin at count, this will work for the rest of the array
        for (int i=count; i < array.length; i++) {
            System.out.println("Element: "+ (i+1));
            array[i] = Integer.parseInt(scanner.nextLine());
            count++;
        }
        System.out.println("Array fill up");
    }

    //Method to put one element at time
    public static void filloneArray(int [] array, int element){
        //Chewck if array is full
        if(count>= array.length){
            System.out.println("Array is full");
            return;
        }
        array[count] = element;
        count++;
        System.out.println("Element: "+element+" added to the array");
    } 

    public static void printArray(int [] array){
        if(count==0){
            System.out.println("There is no elements on the array");
            return;
        }
        for(int i=0; i<array.length; i++){
            System.out.println("|"+"["+array[i]+"]"+"|");
        }
    }

    //Method to find an element in the array
    public static int findElement(int[] array, int element) {
        //Check if is not empty
        if(count == 0 ){
            System.out.println("Array is empty");  
            return -1;
        }else{
            //Binary Search, need to have the array order

            //Order the array first
            //This is for example if the array has lenght 100000, and you only have fill 3 slots, this will only order 0 - 3, and not the rest
            java.util.Arrays.sort(array, 0, count);

            int mid = 0, low=0, high=count-1;
            while(low<=high){
                mid=(low+high)/2;
                if(array[mid]== element){
                    return mid;
                }else if (array[mid]<element){
                    low = mid+1;
                }else if (array[mid]>element) {
                    high = mid-1;
                }
            }
        }
        return -1;
    }
}

