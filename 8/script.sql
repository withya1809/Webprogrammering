USE dat310;
-- DELETE from `products`;

CREATE TABLE if not exists `products`(
    `product_id` int NOT NULL AUTO_INCREMENT,
    `title` varchar(50) NOT NULL,
    `price` int  NOT NULL,
    `discount` int  NOT NULL,
    `img` varchar(50)  NOT NULL,
    `description` varchar(255)  NOT NULL,
    `details` text NOT NULL,
    PRIMARY KEY(`product_id`)
);

 
-- add insert to insert products
-- add create statement for orders and order_rows
CREATE TABLE if not exists `orders`(
    `order_id` int NOT NULL AUTO_INCREMENT,
    `first_name` varchar(50) NOT NULL,
    `last_name` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `street` varchar(50) NOT NULL,
    `city` varchar(50) NOT NULL,
    `postcode` int  NOT NULL,
    PRIMARY KEY(`order_id`)
);
 
CREATE TABLE if not exists `order_row`
(
    `row_id` int NOT NULL AUTO_INCREMENT,
    `product_id` int NOT NULL,
    `order_id` int NOT NULL,
    `count` int  NOT NULL,
    `size` varchar(50) NOT NULL,
    PRIMARY KEY(`row_id`),
    FOREIGN KEY(`product_id`) REFERENCES products(`product_id`),
    FOREIGN KEY(`order_id`) REFERENCES orders(`order_id`)
);
-- add insert to insert products

INSERT INTO products(product_id,title,price,discount,img, description,details) VALUES (NULL, 'Special socks', 170, 18, 'swsock.jpg','Perfectly good socks!', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Namefficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesqueluctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diamnulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollismagna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orcivel augue vehicula rutrum. Nullam vitae sollicitudin orci.');
INSERT INTO products(product_id,title,price,discount,img, description,details) VALUES (NULL, 'Good socks', 170, 0, 'tsock.jpg','Perfectly good socks!', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Namefficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesqueluctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diamnulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollismagna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orcivel augue vehicula rutrum. Nullam vitae sollicitudin orci.');
INSERT INTO products(product_id,title,price,discount,img, description,details) VALUES (NULL, 'Bad socks', 170, 0, 'ssock.jpg','Really Bad socks!', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Namefficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesqueluctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diamnulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollismagna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orcivel augue vehicula rutrum. Nullam vitae sollicitudin orci.');