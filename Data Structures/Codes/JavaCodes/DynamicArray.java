import java.util.Scanner;

public class DynamicArray {

    static int count = 0; //Track how many slots are filled 
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        //Create the initial array 
        System.out.println("Enter the size of the array: ");
        //Ask to the user to enter the size of the array
        int size = Integer.parseInt(scanner.nextLine());

        int[] array = new int[size];

        //Menu
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
                    array = fillArray(array);
                    System.out.println("Array fill up");
                    break;
                case 2:
                    System.out.println("Type the element to put inside");
                    element = Integer.parseInt(scanner.nextLine());
                    array = filloneArray(array, element);
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


    //Method to fill the array with values, this method can be work later
    //for now will not be available 
    public static int[] fillArray(int[] array) {
        //Check if array is full
        if(count >= array.length) {
            //We can copy the logic for one by one element
            int [] newarray = new int [(array.length)*2];
            //Copy all elements
            for (int i=0; i<count; i++){
                newarray[i] = array[i];
            }
            //Now array has to be the same
            array = newarray;
        }
        //After duplicate the array if is necessary
        System.out.println("Enter the elements of the array: ");
        for (int i=count; i<array.length; i++){
            System.out.println("Element: "+ (i+1));
            array[i] = Integer.parseInt(System.console().readLine());
            count++; 
        }    
        return array;
    }

    //Method to put one element at time
    public static int[] filloneArray(int [] array, int element){
        //Check if array is full
        if(count>= array.length){
            //NOw as the array has to be dinamic, now we have to
            //Duplicate the size of the array, so we have to create a new array, and copy all the elements on the one
            int [] newarray = new int [(array.length)*2];
            //Copy all elements
            for (int i=0; i<count; i++){
                newarray[i] = array[i];
            }
            //Now array has to be the same
            array = newarray;
            //WE can print a message saying that we have duplicate the size
            System.out.println("The size of the array has duplicate it, now can fill: "+((array.length/2)-1)+" more elements");
        }
        //After we do the last comparasion we can now put the new element on the "new array"
        array[count] = element;
        count++;
        System.out.println("Element: "+element+" added to the array");
        return array;
    } 

    //Se the elements on the array
    public static void printArray(int [] array){
        if(count==0){
            System.out.println("There is no elements on the array");
            return;
        }
        //If we only wanted to see the elements on the array filled by us "i<count" if wanted to the all the slots
        //Even if we have not fill them, then "i<array.length"
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

