<body>
    <h1>ASCII Table Generator</h1>
    <h3>Ascii Table generator</h3>
    <div>
        This is a basic library to let the user generate an ASCII table given headers and row data.<br /><br />
        <b>Usage:</b>
        <div  style="background-color: #e2e2e2; max-width: fit-content; padding-left: 20px; padding-right: 20px; white-space: pre;">
            from TableGenerator import Table<br  />
            t = Table("These", "are", "the", "table", "headers") # Create the table headers<br  />
            t.addRow("This", "is", "data") # 2 empty cells after<br  />
            t.addRow("Here", "is", "some", "more", "data") # All cells are filled<br  />
            t.addRow("a", "b", "c", "d", "e", "f") # Since there are only 5 headers, the last element is dropped<br  />
            t.print() # Print the table
    </div>
</body>