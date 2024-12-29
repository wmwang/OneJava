//A2題形-繼承與多型 (加入動態新增動物的功能)

import java.util.ArrayList;
import java.util.Scanner;

abstract class Animal {
    String name;

    public Animal(String name) {
        this.name = name;
    }

    public abstract void makeSound();
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(name + " says: Woof Woof!");
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(name + " says: Meow Meow!");
    }
}

public class AnimalTester {
    public static void main(String[] args) {
        ArrayList<Animal> animals = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter animal type (dog/cat) or 'exit' to quit: ");
            String type = scanner.nextLine();

            if (type.equalsIgnoreCase("exit")) {
                break;
            }

            System.out.print("Enter the name of the animal: ");
            String name = scanner.nextLine();

            if (type.equalsIgnoreCase("dog")) {
                animals.add(new Dog(name));
            } else if (type.equalsIgnoreCase("cat")) {
                animals.add(new Cat(name));
            } else {
                System.out.println("Unknown animal type. Please enter 'dog' or 'cat'.");
            }
        }

        System.out.println("\nAnimal sounds:");
        for (Animal animal : animals) {
            animal.makeSound();
        }
    }
}
