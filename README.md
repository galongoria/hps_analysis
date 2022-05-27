# HPS Invoice Data Analysis #

This was an independent project that analyzed sales data from invoices at an HVAC company. This was my introduction into data collection, cleaning, and analysis. As such, some of the methods are crude, and I plan on improving the code if I find it useful in other applications.



Step 1 – Collection:

The method for naming invoices and estimates changed over time, so I normalized the file names. Then, I found invoices as far back as I could and organized them into a single directory.

Step 2 – Cleaning:

The invoice number, date, and customer name, phone number, address, and email are located in the same cells for every invoice. So I just took that data into a new dataframe. However, the invoice amount changes because the lines in an invoice are at least a certain size and can become larger if there was a lot done. To get the total, I referenced the cell next to the dollar amount which is a string that says "TOTAL" and put that in a column named "amount."

Step 3 – Analysis:

#### do later



