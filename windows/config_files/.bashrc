export PATH=$HOME:$PATH
parse_git_branch() {
  branch=$(git symbolic-ref --short HEAD 2>/dev/null)
  if [ -n "$branch" ]; then
    echo "($branch)"
  fi
}

PS1='\[\033[38;5;129m\]\w\[\033[0m\] \[\033[38;5;33m\]$(parse_git_branch)\[\033[0m\] '


