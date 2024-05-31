UPDATE_SNAPSHOT_BRANCH_NAME="hj/test_branch"
existed_in_remote=$(git ls-remote --heads origin $UPDATE_SNAPSHOT_BRANCH_NAME)
if [[ -z ${existed_in_remote} ]]; then
  echo "doesnn't exist"
  exit 1
else
  echo "exists"
  exit 0
fi