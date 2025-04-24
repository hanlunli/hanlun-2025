---
layout: post
title: HW
permalink: /collections_hw
comments: True
---

```Java
import java.util.*;

class Collectible {
    private String name;
    private String type;
    private int rarity;

    public Collectible(String name, String type, int rarity) {
        this.name = name;
        this.type = type;
        this.rarity = rarity;
    }

    public String getName() { return name; }
    public String getType() { return type; }
    public int getRarity() { return rarity; }

    public String toString() {
        return name + " [" + type + "] (Rarity: " + rarity + ")";
    }

    // For use in HashMap/HashSet
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Collectible)) return false;
        Collectible that = (Collectible) o;
        return name.equals(that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}

class Inventory {
    private ArrayList<Collectible> items;
    private Set<String> tradedItems;
    private Set<String> duplicateItems;
    private Map<Collectible, Double> itemValues;
    private Stack<String> folderPath;

    public Inventory() {
        items = new ArrayList<>();
        tradedItems = new HashSet<>();
        duplicateItems = new HashSet<>();
        itemValues = new HashMap<>();
        folderPath = new Stack<>();
    }

    public void addItem(Collectible c) {
        items.add(c);
    }

    public void addItems(List<Collectible> newItems) {
        items.addAll(newItems);
    }

    public void removeItems(List<Collectible> removeList) {
        items.removeAll(removeList);
    }

    public void showInventory() {
        for (Collectible c : items) {
            System.out.println(c);
        }
    }

    public int countByType(String type) {
        int count = 0;
        for (Collectible c : items) {
            if (c.getType().equalsIgnoreCase(type)) {
                count++;
            }
        }
        return count;
    }

    public void setValue(Collectible c, double value) {
        itemValues.put(c, value);
    }

    public void updateValuesByRarity(int targetRarity, double percentIncrease) {
        for (Map.Entry<Collectible, Double> entry : itemValues.entrySet()) {
            if (entry.getKey().getRarity() == targetRarity) {
                double newValue = entry.getValue() * (1 + percentIncrease / 100.0);
                itemValues.put(entry.getKey(), newValue);
            }
        }
    }

    public List<Collectible> filterByRarity(int rarity) {
        List<Collectible> result = new ArrayList<>();
        for (Collectible c : items) {
            if (c.getRarity() == rarity) {
                result.add(c);
            }
        }
        return result;
    }

    public void addUniqueItem(Collectible c) {
        String name = c.getName();
        if (tradedItems.contains(name)) {
            duplicateItems.add(name);
        } else {
            items.add(c);
            tradedItems.add(name);
        }
    }

    public void displayCollection() {
        System.out.printf("%-20s %-10s %-10s %-10s%n", "Name", "Type", "Rarity", "Value");
        for (Collectible c : items) {
            double value = itemValues.getOrDefault(c, 0.0);
            System.out.printf("%-20s %-10s %-10d $%-10.2f%n", 
                c.getName(), c.getType(), c.getRarity(), value);
        }
    }

    public void goDeeper(String folder) {
        folderPath.push(folder);
        System.out.println("Current Path: " + String.join(" > ", folderPath));
    }

    public void goBack() {
        if (!folderPath.isEmpty()) {
            folderPath.pop();
        }
        System.out.println("Current Path: " + String.join(" > ", folderPath));
    }
}

public class Main {
    public static void main(String[] args) {
        Inventory myInventory = new Inventory();

        Collectible c1 = new Collectible("Phoenix Flame", "Fire", 5);
        Collectible c2 = new Collectible("Aqua Sprite", "Water", 3);
        Collectible c3 = new Collectible("Blazing Ember", "Fire", 2);

        myInventory.addItem(c1);
        myInventory.addItem(c2);
        myInventory.addItem(c3);

        myInventory.setValue(c1, 50.0);
        myInventory.setValue(c2, 30.0);
        myInventory.setValue(c3, 10.0);

        myInventory.showInventory();
        System.out.println("Fire-type count: " + myInventory.countByType("Fire"));

        System.out.println("\nUpdated Values for Rarity 5 (10% increase):");
        myInventory.updateValuesByRarity(5, 10);
        myInventory.displayCollection();

        System.out.println("\nFilter Rarity 3:");
        for (Collectible c : myInventory.filterByRarity(3)) {
            System.out.println(c);
        }

        System.out.println("\nAdding duplicate item:");
        myInventory.addUniqueItem(c1); // duplicate

        System.out.println("\nFolder Navigation:");
        myInventory.goDeeper("Weapons");
        myInventory.goDeeper("Magic");
        myInventory.goDeeper("Fire");
        myInventory.goBack();
    }
}
```
