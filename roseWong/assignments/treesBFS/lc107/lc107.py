# Problem Statement #

# Given a binary tree, populate an array to represent its level-by-level 
# traversal in reverse order, i.e., the lowest level comes first. 
# You should populate the values of all nodes in each level 
# from left to right in separate sub-arrays.

# traverse the binary tree from top to bottom.
# Store all values in a queue
# pop the queue to reverse the list of values

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  
  if root is None:
    return root

  queue = []
  return_list = []

  queue.append(root)
  while len(queue) > 0:
    ans = []
    l = len(queue)

    for l in range(l):
      node = queue.pop(0)
      ans.append(node.val)

      if node.left != None:
        queue.append(node.left)

      if node.right != None:
        queue.append(node.right)
        return_list.append(ans)
        
  return return_list

  # reversedList = []
  # while len(return_list) > 0:
  #   reversedList.append(return_list.pop(len(return_list)-1))
  
  # return reversedList



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()







# Solution
# -----
# def traverse(root):
#   result = deque()
#   if root is None:
#     return result

#   queue = deque()
#   queue.append(root)
#   while queue:
#     levelSize = len(queue)
#     currentLevel = []
#     for _ in range(levelSize):
#       currentNode = queue.popleft()
#       # add the node to the current level
#       currentLevel.append(currentNode.val)
#       # insert the children of current node in the queue
#       if currentNode.left:
#         queue.append(currentNode.left)
#       if currentNode.right:
#         queue.append(currentNode.right)

#     result.appendleft(currentLevel)

#   return result

# -----

# Time complexity #
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space complexity #
# The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.
