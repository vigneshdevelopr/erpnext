# import frappe

# def on_submit(doc, method):
#     for item in doc.items:
#         if item.item_code == "ttset":  # Check if the selected item is "Tapping Tool Set"
#             tapping_tool = frappe.get_doc("Item", "Tapping_Tool")
#             if tapping_tool.variants:
#                 for variant in tapping_tool.variants:
#                     doc.append("items", {
#                         "item_code": variant.item_code,
#                         "item_name": variant.item_name,
#                         "rate": variant.rate,
#                         "qty": item.qty
#                     })

#     # Save the updated purchase order
#     doc.save()
