export default function ({ $axios, redirect, $sentry }, inject) {
  // Create a custom axios instance
  const api = $axios.create({});
  api.onError(error => {
    console.error(error);
    $sentry.captureException(error);
    redirect('/400');
  });

  // Set baseURL to something different
  api.setBaseURL(process.env.API_AUDIENCE || 'https://localhost:8000');

  // Inject to context as $api
  inject('api', api);
}
