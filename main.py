import tkinter as tk
import json

# this is a test

# main
def main():
    # Load conversionData.json
    with open("conversionData.json", "r") as f:
        conversionData = json.load(f)

    # Initialize tkinter
    window = tk.Tk()
    window.title("UselessUnitConverter")
    window.geometry("300x150")
    window.resizable(False, False)

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    window.columnconfigure(2, weight=1)

    # Caption 
    tk.Label(text="UselessUnitConverter").grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Handle category selection
    def selectCategory(selectedCategory):
        print("Selected unit:", selectedCategory)
        # This code block should only be called once per program run, but idc
        inputUnitOption.config(state='normal')
        outputUnitOption.config(state='normal')
        inputValue.config(state='normal')

        units = list(conversionData[selectedCategory].keys())
        print(units)
        # Reset unit options
        inputUnitOption["menu"].delete(0, "end")
        outputUnitOption["menu"].delete(0, "end")
        for unit in units:
            inputUnitOption["menu"].add_command(label=unit, command=tk._setit(selectInputUnit, unit, convert)) 
            outputUnitOption["menu"].add_command(label=unit, command=tk._setit(selectOutputUnit, unit, convert))
        
        selectInputUnit.set("Select Unit")
        selectOutputUnit.set("Select Unit")

    # Handle numeric input
    def FloatValidator(S):
        if S == "": 
            return True
        elif S.replace('.','',1).isdigit():
            # Trigger conversion on update
            convert(S)
            return True
        else: 
            return False 
        
    valid = window.register(FloatValidator)

    # Handle conversion
    def convert(input):
        print("convert", input)
        
        # Category should always be present at this point
        category = selectCategoryUnit.get()

        # Get input value from function or textbox
        if (input and input.replace('.','',1).isdigit()):
            input = float(input)
        elif inputValue.get().replace('.','',1).isdigit():
            input = float(inputValue.get())
        else: 
            # No input value
            return

        # Get input unit
        inputUnit = selectInputUnit.get()
        if (not inputUnit or inputUnit == "Select Unit"):
            # No input unit
            return

        # Get output unit
        outputUnit = selectOutputUnit.get()
        if (not outputUnit or outputUnit == "Select Unit"):
            # No output unit
            return

        # Get conversion
        factorInput = conversionData[category][inputUnit]["value"]
        factorOutput = conversionData[category][outputUnit]["value"]

        # Get output
        output = input * factorInput / factorOutput

        # Set output
        outputValue.config(state='normal')
        outputValue.delete(0, "end")
        outputValue.insert(0, output)
        outputValue.config(state='readonly')

    # Create category selection
    selectCategoryUnit = tk.StringVar()
    selectCategoryUnit.set("Select a category")
    categorySelectOption = tk.OptionMenu(window, selectCategoryUnit, *list(conversionData.keys()), command=selectCategory)
    categorySelectOption.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

    # Create input
    tk.Label(window, text="Input").grid(row=2, column=0, columnspan=1)
    inputValue = tk.Entry(window, validate='key', validatecommand=(valid, "%P"), state='disabled')
    inputValue.grid(row=2, column=1, columnspan=1)

    selectInputUnit = tk.StringVar()
    selectInputUnit.set("Select Unit")
    inputUnitOption = tk.OptionMenu(window, selectInputUnit, [], command=convert)
    inputUnitOption.config(state='disabled')
    inputUnitOption.grid(row=2, column=2, columnspan=1)


    # Create output
    tk.Label(window, text="Output").grid(row=3, column=0, columnspan=1)
    outputValue = tk.Entry(window, state='readonly')
    outputValue.grid(row=3, column=1, columnspan=1)

    selectOutputUnit = tk.StringVar()
    selectOutputUnit.set("Select Unit")
    outputUnitOption  = tk.OptionMenu(window, selectOutputUnit, [])
    outputUnitOption.config(state='disabled')
    outputUnitOption.grid(row=3, column=2, columnspan=1)

    # Execute tkinter
    window.mainloop()

if __name__ == '__main__':
    main()
