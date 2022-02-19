def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  w_start = 0
  w_sum = 0
  max_sum = float('-inf')
  for i in range(len(arr)):
    w_sum += arr[i]
    if i >= k-1:
      max_sum = max(max_sum, w_sum)
      w_sum -= arr[w_start]
      w_start += 1
  return(max_sum)