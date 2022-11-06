import reactToWebComponent from "react-to-webcomponent";
import React from "react";
import ReactDOM from "react-dom/client";
import reactComponents from "./index";

/**
 * Export all components as Web Components
 *
 * The bundled version of this script can be imported from any website, and it
 * will allow use of the visualizations with custom element html tags.
 *
 * https://developer.mozilla.org/en-US/docs/Web/Web_Components
 *
 * @example
 * ```html
 * <circuitsvis-hello name="Bob"/>
 * ```
 */
Object.keys(reactComponents).forEach((componentName: string) => {
  // Create the web component
  const component = reactComponents[componentName];
  const WebComponent = reactToWebComponent(
    component,
    React as any,
    ReactDOM as any,
    {
      shadow: true
    }
  );

  // Generate the name
  const name = `circuitsvis-${componentName
    .replace(/[^a-zA-Z]+/g, "")
    .toLowerCase()}`;

  // Set the custom element
  try {
    customElements.define(name, WebComponent as any);
  } catch (err) {
    // eslint-disable-next-line no-console
    console.error(err);
  }
});
