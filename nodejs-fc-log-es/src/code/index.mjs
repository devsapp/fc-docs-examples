
export const handler = async (event, context) => {
  process.stdout.write('hi,fc\n');
  console.log('hello,world');
  context.logger.info('hello,fc');
  return "Hello World!";
};