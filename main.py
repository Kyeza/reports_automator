from os import listdir

from comment_personalize import comment_personalize


# read raw comments from txt files into dict
filenames = [f for f in listdir('./') if '_comments' in f]
raw_comments = {}
for filename in filenames:
  with open(filename, mode='r') as f:
    filename = filename.rstrip('.txt')
   raw_comments[filename] = f.readlines()

# format comments 
formatted_comments = {}
for key, value in raw_comments.items():
  value = list(filter('\n'.__ne__, value))
  value = list(map(lambda x: x.rstrip(), value))
  formatted_comments[key] = {}
  for option in value:
    formatted_comments[key][int(option[0])] = option[3:]
   
print(formatted_comments)

# welcome
print('Welcome to BlitzThatReport')
print('(Enter Q to quit)\n(Enter \'0\' to skip a comment)\n')
while True:
  # initial inputs
  name = str(input('Enter pupil name: ')).title()
  if name == 'Q':
    break
  
  gender_choice = str(input('M/F: ')).upper()
  # process gender variations
  if gender_choice == 'M':
    gender = 'he'
    gender_title = gender.title()
    gender_possess = 'his'
    gender_possess_title = gender_possess.title()
    gender_self = 'himself'
  elif gender_choice == 'F':
    gender = 'she'
    gender_title = gender.title()
    gender_possess = 'her'
    gender_possess_title = gender_possess.title()
    gender_self = 'herself'
  else:
    print('Invalid gender!\n')
    continue
  
  # initialize/reset empty report
  report = ''
  # select and personalize general comment
  general_choice = int(input('Choose general comment: '))
  if general_choice != 0:
    general_comment = general_comments[general_choice] 
    general_comment = comment_personalize(
      general_comment,
      name, 
      gender, 
      gender_title,
      gender_possess, 
      gender_possess_title,
      gender_self
    )
    # add general comment to end of current report
    report += (general_comment + ' ')

  # select and personalize target comment
  target_choice = int(input('Choose target comment: '))
  if target_choice != 0:
    target_comment = targets_comments[target_choice] 
    target_comment = comment_personalize(
      target_comment,
      name, 
      gender, 
      gender_title,
      gender_possess, 
      gender_possess_title,
      gender_self
    )
    # add target comment to end of current report
    report += (target_comment + ' ')

# select and personalize other comment
  other_choice = int(input('Choose other comment: '))
  if other_choice != 0:
    other_comment = others_comments[other_choice] 
    other_comment = comment_personalize(
      other_comment,
      name, 
      gender, 
      gender_title,
      gender_possess, 
      gender_possess_title,
      gender_self
    )
    # add target comment to end of current report
    report += (other_comment + ' ')

  # select and personalize conclude comment
  conclude_choice = int(input('Choose conclude comment: '))
  if conclude_choice != 0:
    conclude_comment = concludes_comments[conclude_choice] 
    conclude_comment = comment_personalize(
      conclude_comment,
      name, 
      gender, 
      gender_title,
      gender_possess, 
      gender_possess_title,
      gender_self
    )
    # add target comment to end of current report
    report += (conclude_comment + ' ')

  # display report
  print('\n', report, '\n')
  # write to output.txt
  while True:
    write_choice = str(input('Write to file Y/N: ')).upper()
    if write_choice == 'Y':
      with open('./output.txt', mode='a') as f:
        f.write(name + '\n\n' + report + '\n\n')
      print('\n')
      break
    elif write_choice == 'N':
      break
    else:
      print('Invalid choice! Y/N: ')
      continue



  