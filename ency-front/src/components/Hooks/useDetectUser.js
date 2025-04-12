const useDetectUser = async () => {
  try {
    const res = await fetch("api/v1/auth_check");
    const logs = res.json();
    return logs;
  } catch (err) {
    console.error(err);    
  }
}

export default useDetectUser;
