import JSON

println("""
 _   _          _              _   _       _ _    ____                          _
| | | |___  ___| | ___ ___ ___| | | |_ __ (_| |_ / ___|___  _ ____   _____ _ __| |_ ___ _ __
| | | / __|/ _ | |/ _ / __/ __| | | | '_ \\| | __| |   / _ \\| '_ \\ \\ / / _ | '__| __/ _ | '__|
| |_| \\__ |  __| |  __\\__ \\__ | |_| | | | | | |_| |__| (_) | | | \\ V |  __| |  | ||  __| |
 \\___/|___/\\___|_|\\___|___|___ \\___/|_| |_|_|\\__ \\____\\___/|_| |_|\\_/ \\___|_|   \\__\\___|_|
""")

# Load the JSON file with the values
conversionData = JSON.parse(open("conversionData.json"))

# Get & print keys (avaiable methods)
methods = collect(keys(conversionData))

for (index, value) in enumerate(methods)
    println("[$(index)] $value")
end

# Mode selector
print("Select a method: ")
selectedMethod = nothing 
while (isnothing(selectedMethod))
    global selectedMethod = tryparse(Int, readline())
    
    if (isnothing(selectedMethod))
        print("Please select a method")
        global selectedMethod = nothing
    elseif (isa(selectedMethod, Number))
        break
        if (selectedMethod < 1 || selectedMethod > len(methods))
            print("Please select a valid method")
            global selectedMethod = nothing
        end
    end
end

println("You selected: $(methods[selectedMethod])")
println("")

# Input Value & Unit selector
println("Avaiable Units:")
selectedUnits = conversionData[methods[selectedMethod]]
for (index, value) in enumerate(selectedUnits)
    local name = value[2]["name"]
    local short = value[1]
    println("[$short] $name")
end
println("Select source count and source unit (e.g. '1 cm'): ")

inputUnit = nothing
inputValue = nothing

while isnothing(inputValue)
    local input = readline()
    local splitInput = split(strip(input), " ")
    global inputValue =  tryparse(Float64, splitInput[1])
    global inputUnit = splitInput[2]
    
    if (isa(inputValue, Number) && haskey(selectedUnits, inputUnit))
        break
    else 
        println("Please both values in the correct format, e.g. \"1 cm\"\n")
        global inputValue = nothing
    end
end

println("Select target unit: ")
targetUnit = nothing

while isnothing(targetUnit)
    global targetUnit = strip(readline())
    if (haskey(selectedUnits, targetUnit))
        break
    else 
        println("Please select a valid unit\n")
        global targetUnit = nothing
    end
end

println("")
inputUnitLong = selectedUnits[inputUnit]["name"]
targetUnitLong = selectedUnits[targetUnit]["name"]
println("Converting $(inputValue) $(inputUnitLong) to $(targetUnitLong)...")
targetValue = inputValue * selectedUnits[inputUnit]["value"] / selectedUnits[targetUnit]["value"] 
println("$(inputValue) $(inputUnitLong) is $(targetValue) $(targetUnitLong)")

println("Program finished gracefully")