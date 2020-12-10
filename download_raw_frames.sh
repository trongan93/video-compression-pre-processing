LOCAL_FRAMES_DATA_PATH="/mnt/d/VideoData"

download_frames(){
  local BASE_URL=${1}
  local LOCAL_URL=${2}
  local START_ID=${3}
  local END_ID=${4}

  cd "${LOCAL_URL}"

  for i in $(seq -w ${START_ID} ${END_ID})
  do
    echo "In downloading file "${BASE_URL}/${i}.png" to ${LOCAL_URL}"
    wget "${BASE_URL_1}/${i}.png"
  done
}

#Download frames
BASE_URL_1="https://media.xiph.org/sintel/sintel-1080-png"
LOCAL_URL_1="${LOCAL_FRAMES_DATA_PATH}/sintel/sintel-1080-png/"
START_ID_1=00000001
END_ID_1=00021312
mkdir -p "${LOCAL_URL_1}"
download_frames "${BASE_URL_1}" "${LOCAL_URL_1}" "${START_ID_1}" "${END_ID_1}"
