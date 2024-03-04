export const handler = async (event, context) => {
  return "Hello FC!";
};

export const initialize = async (event, context) => {
  console.log('initializer');
  return "";
}

export const preStop = async (event, context) => {
  console.log('preStop');
  return "";
}
