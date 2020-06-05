/* global MusicKit */

export default async context => {
	// Handle init
	if (MusicKit) {
		await context.store.dispatch('nuxtClientInit', context);
	} else {
		document.addEventListener('musickitloaded', async () => {
			await context.store.dispatch('nuxtClientInit', context);
		});
	}
};
