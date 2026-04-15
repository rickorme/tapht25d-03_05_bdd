Feature: Inventory Management System

    Scenario: Adding a new product to the stock
        Given the stock is currently empty
        When I add a product named "Mac mini M4" with an amount of 20
        Then the stock should contain 1 item
        And the product "Mac mini M4" should have an amount of 20

    Scenario: Reducing the quantity of a specific product
        Given the stock already contains a product named "Macbook Neo" with an amount of 20
        When I reduce the amount of "Macbook Neo" by 1
        Then the product "Macbook Neo" should have an amount of 19

    Scenario: Reducing quantity by more than stock quantity
        Given the stock already contains a product named "Macbook Neo" with an amount of 1
        When I reduce the amount of "Macbook Neo" by 2
        Then I should get an error saying there is not enough in stock