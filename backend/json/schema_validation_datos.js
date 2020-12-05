
db.createCollection("menus",
    {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                required: ["name", "price", "descriptionMenu", "ingredients", "category"],
                properties: {
                    name: {
                        bsonType: "string",
                        description: "must be a string with name of menu"
                    },
                    price: {
                        bsonType: "double",
                        description: "must be a double with the price of menu"
                    },
                    descriptionMenu: {
                        bsonType: "string",
                        description: "must be a string with description of menu"
                    },
                    ingredients: {
                        bsonType: "array",
                        description: "must be an array with ingredients of menus",
                        items: {
                            bsonType: "string",
                            description: "must be a string with ingredient of menu"
                        }
                    },
                    category: {
                        bsonType: "string",
                        description: "must be a string with category of menu"
                    }
                }
            }
        }
    }
)
