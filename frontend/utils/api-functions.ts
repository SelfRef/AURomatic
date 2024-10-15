export async function streamResponseToVariable(response: Response, data: { [x: string]: string; }, prop: string) {
	if (!response) return
	if (!response.body) return
	for await (const chunk of response.body.values()) {
		data[prop] += new TextDecoder().decode(chunk);
	}
}