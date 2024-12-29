//========================================================================
//題目說明：請協助將以下java 程式轉換為Python
//
//提示(題目組內部參考)：集合操作 (計算不重複數字的總和)
//
//題目Input： ./java/A2-5.java
//
//題目Output： 生成的檔案需為 ./java/A2-5-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A2-5 container，可自動將./java/A2-5-answer.py程式在python 3.x環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A2-5
//
//驗證： 校驗腳本將分別對A2-5.java、A2-5-answer.py 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

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

