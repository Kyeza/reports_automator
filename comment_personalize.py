# personalize comments
def comment_personalize(generic_comment, name, gender, gender_title, gender_possess, gender_possess_title, gender_self):
  return (generic_comment
    .replace('[name]', name)
    .replace('[gender]', gender)
    .replace('[gender_title]', gender_title)
    .replace('[gender_possess]', gender_possess)
    .replace('[gender_possess_title]', gender_possess_title)
    .replace('[gender_self]', gender_self)
  )
