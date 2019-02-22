elements = input().split(' ')

length_of_elements = int(len(elements) / 2)
counter = 1
index_of_front_elements = 0
index_of_back_elements = len(elements) - 1

while (counter <=length_of_elements):
      front_element = elements[index_of_front_elements]
      back_element = elements[index_of_back_elements]

      elements[index_of_front_elements] = back_element
      elements[index_of_back_elements] = front_element

      index_of_front_elements += 1
      index_of_back_elements -= 1

      counter += 1

for element in elements:
    print(element, end=' ')